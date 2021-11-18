# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import argparse
import os
import subprocess
import sys
import shlex


def run(command: str, check=True, silent=False) -> subprocess.CompletedProcess:
    """
    Runs a command provided as a string
    
    :param command: Command provided as a string
    :param check: If true, will throw exception on failure
    :param silent: If set to True, the output won't be printed.

    :return: CompleteProcess instance - the result of the command executed
    """

    if not silent:
        log_msg = f"Executing: {command}" + os.linesep
        print(log_msg, end=os.linesep, file=sys.stderr)
    
    # https://docs.python.org/3/library/subprocess.html
    proc = subprocess.run(shlex.split(command), check=check)

    return proc
    

def build_site():
    run('which git')

def parse_args():
    parser = argparse.ArgumentParser(description='Build Airflow website')
    parser.add_argument("action", choices=['build-site', 'stop'], default="build-site", nargs="?")

    args = parser.parse_args()
    return args


def main():
    """
    Main function of the script
    """
    args = parse_args()

    if args.action == 'build-site':
        build_site()
    elif args.action == 'stop':
        print("do nothing")
        sys.exit(1)
    


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print("Script failed to run")
        raise err

