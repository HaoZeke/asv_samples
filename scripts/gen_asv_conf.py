import argparse
import json5
import json
import subprocess
import sys

def get_current_git_branch():
    """Returns the current Git branch name."""
    try:
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        return branch_name
    except subprocess.CalledProcessError as e:
        print(f"Error obtaining current Git branch: {e}")
        return None

def generate_asv_config(base_config_path):
    """Generates asv.conf.json using the current Git branch."""
    current_branch = get_current_git_branch()
    if current_branch is None:
        print("Could not determine current Git branch. Exiting.")
        sys.exit(1)

    with open(base_config_path, 'r') as base_file:
        config = json5.load(base_file)

    config['branches'] = [current_branch]

    with open('asv.conf.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

    print(f"asv.conf.json has been generated with the current branch: {current_branch}")

def main():
    parser = argparse.ArgumentParser(description="Generate asv.conf.json from asv.conf.base.json with the current Git branch.")
    parser.add_argument("base_config_path", help="Path to asv.conf.base.json file")
    args = parser.parse_args()

    generate_asv_config(args.base_config_path)

if __name__ == "__main__":
    main()
