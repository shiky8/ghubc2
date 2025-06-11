# ghubc2

> A dumb tool that uses GitHub as a C2 (Command-and-Control).

This script uses a GitHub repository to send commands to a remote machine and retrieve the output.  
It updates a file (`sender.txt`) with the command to execute, and the output is saved to another file (`resver.txt`) in the same repository.

---

## ⚠️ WARNING

   This tool is intended strictly for educational or authorized security testing purposes. Unauthorized use of this software may violate laws. Always obtain proper permission before conducting any testing.

---

## 🚀 Usage

1. **Configuration**  
   Replace these variables in the script:
   ```python
   access_token = "YOUR_ACCESS_TOKEN"
   repo_id = "username/repo"
   branch = "main"
   * `access_token`: Your GitHub personal access token (with repo permissions).

   * `repo_id`: The repository to use (e.g., username/repo).

   * `branch`: The branch where sender.txt and resver.txt are located.

2. **Creating a Private C2 Repo**
   
      You can create a fake GitHub account and make a private repository as your C2 channel.
      Generate an access token with permissions only for this private repo for additional security.

4. **Install Dependencies**
   ```bash
   pip install PyGithub
   ```
5. **Run the script**
   ```bash
   python3 ghubc2.py
   ```
6. **How it works**

   *  The script continuously reads commands from sender.txt in the GitHub repo.

   *  Executes the commands on the system where it’s running.

   *  Saves the command output to resver.txt in the repo.

   *  If the command is "killme", the script stops.

---

## Proof of Concept (PoC)
https://github.com/user-attachments/assets/7301c6b2-96b9-42d1-b334-26a1acbe3977

---

## ⚠️ Important Considerations

   *   Security: This tool executes arbitrary commands from a remote repository—it can be extremely dangerous.
   *   Never run it on a production or personal system without fully understanding the risks.

   *   GitHub API Limits: Frequent API calls can quickly reach GitHub's rate limits, especially if using a free account.

   *   Persistence: If the script stops, you must manually restart it.

   *   Private Repo: To avoid detection and misuse, use a private repository. Make sure your GitHub access token is scoped as narrowly as possible.

   *   Legal & Ethical Use:
   *   This tool is intended for educational and demonstration purposes only.
   *   Using it for malicious or unauthorized activities is illegal and unethical.

---

## 📄 Repository File Structure

   ```pgsql
   repo/
   ├── sender.txt   # file with commands to execute
   └── resver.txt   # file where command output is written
   ```
