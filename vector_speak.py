#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
# Copyright (c) 2018 Keith Prickett
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Vector Speak

Make Vector say whatever you type.
"""

import anki_vector

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        while 1:
            raw_input = input("What do you want Vector to say?>")
            if len(raw_input) > 0:
                if raw_input in ['quit', 'exit', 'quit()', 'exit()']:
                    """Quits the program."""
                    print("Bye! Thanks for playing with me!")
                    robot.say_text("Bye! Thanks for playing with me!")
                    raise SystemExit
                else:
                    print("Say '"+raw_input+"'...")
                    robot.say_text(raw_input)


if __name__ == "__main__":
    main()
