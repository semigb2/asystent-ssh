import paramiko
import openai
import json
import readline

def read_settings(filename):
    settings = {}

    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split(": ")
            settings[key] = value

    return settings

def gpt3_query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def analyze_gpt3_response(response):
    commands = response.split('\n')
    commands = [cmd.strip() for cmd in commands if cmd.strip()]
    return commands

def execute_on_debian(commands, hostname, username, password, show_command=False, auto_install=False):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    for command in commands:
        command = command.strip()

        # Jeśli command zaczyna się od cyfry i kropki, traktujemy to jako komentarz
        if command[0].isdigit() and command[1] == '.':
            print(f"\nComment: {command}")
            continue

        if command.startswith("sudo"):
            command = command[5:].strip()

        if show_command:
            print(f"\nCommand: {command}")
        else:
            if not auto_install:
                while True:
                    user_input = input(f"Czy chcesz wykonać polecenie '{command}'? [tak/nie/anuluj] ")
                    if user_input.lower() == "t":
                        break
                    elif user_input.lower() == "n":
                        print(f"Skipped command: {command}")
                        break
                    elif user_input.lower() == "a":
                        ssh.close()
                        print("Anulowano wykonywanie poleceń.")
                        return

        stdin, stdout, stderr = ssh.exec_command(command)
        for line in iter(stdout.readline, ""):
            print(line.strip())

        output = stdout.read().decode('utf-8')
        print(f"Output for '{command}':\n{output}")

    ssh.close()

def communicate_with_user(prompt):
    return input(prompt)

def save_interaction_history(gpt3_prompt, gpt3_response, commands):
    interaction = {
        "gpt3_prompt": gpt3_prompt,
        "gpt3_response": gpt3_response,
        "commands_executed": commands
    }

    with open("interaction_history.json", "a+") as f:
        f.write(json.dumps(interaction) + "\n")

def show_command(commands):
    for command in commands:
        command = command.strip()
        if command.startswith("sudo"):
            command = command[5:].strip()

        print(f"\nCommand: {command}")

def pytanie(prompt):
    if prompt.strip()[-1] != "?":
        print("To nie jest pytanie. Proszę, dodaj znak zapytania na końcu.")
        return None
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

def main():
    settings = read_settings("ustawienia.txt")
    openai.api_key = settings["api_key"]

    readline.read_history_file('history.txt')

    problem_description = communicate_with_user("Opisz swój problem: ")
    auto_install = problem_description.lower().startswith('i ')  # Dodajemy detekcję 'i ' na początku opisu problemu
    if auto_install:
        problem_description = problem_description[2:].strip()

    gpt3_prompt = f"Mam problem z serwerem Debian 11.5: {problem_description}. Jak mogę to rozwiązać?"
    gpt3_response = gpt3_query(gpt3_prompt)

    if "?" in gpt3_response:
        print(gpt3_response)
    else:
        commands = analyze_gpt3_response(gpt3_response)

        show_command(commands)

        execute_on_debian(commands, settings["localhost"], settings["username"], settings["password"], show_command=False, auto_install=auto_install)

        readline.write_history_file('history.txt')

        save_interaction_history(gpt3_prompt, gpt3_response, commands)

if __name__ == "__main__":
    main()

