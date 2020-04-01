import sys, os
from skillshare import Skillshare
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 

___________           .__          .__            ___________   .__.__  .__         .__                             ___ ___                __    
\__    ___/___   ____ |  |_________|__| _____    /   _____/  | _|__|  | |  |   _____|  |__ _____ _______   ____    /   |   \_____    ____ |  | __
  |    |_/ __ \_/ ___\|  |  \_  __ \  |/     \   \_____  \|  |/ /  |  | |  |  /  ___/  |  \\__  \\_  __ \_/ __ \  /    ~    \__  \ _/ ___\|  |/ /
  |    |\  ___/\  \___|   Y  \  | \/  |  Y Y  \  /        \    <|  |  |_|  |__\___ \|   Y  \/ __ \|  | \/\  ___/  \    Y    // __ \\  \___|    < 
  |____| \___  >\___  >___|  /__|  |__|__|_|  / /_______  /__|_ \__|____/____/____  >___|  (____  /__|    \___  >  \___|_  /(____  /\___  >__|_ \
             \/     \/     \/               \/          \/     \/                 \/     \/     \/            \/         \/      \/     \/     \/                                           
                                                                                                                                                                    


				Visit Us for more Cool Stuff: https://thetechrim.com/

                """)


if __name__ == "__main__":
    info()
    main()
