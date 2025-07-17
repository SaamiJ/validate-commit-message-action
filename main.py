import os
import re


def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}\n')
    f.close()    


def main():
    commit_message = os.environ.get("INPUT_COMMITMESSAGE", "").strip()
    print(f"Commit message: '{commit_message}'")

    pattern = r"^(feat|fix|docs): .+"
    is_valid = bool(re.match(pattern, commit_message))

    if is_valid:
        set_github_action_output("outcome", "valid")
    else:
        set_github_action_output("outcome", "invalid")


if __name__ == "__main__":
    main()
