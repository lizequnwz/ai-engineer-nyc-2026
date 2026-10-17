# Create a GitHub repository and upload this package

Recommended repository name: `ai-engineer-nyc-2026`.

Use **Private** for the complete package: it includes your Fidelity application context and personal-project review. No public-redaction pass has been applied.

## 1. Create an empty repository

1. Sign in to GitHub and open [New repository](https://github.com/new).
2. Choose your account or organization and enter the repository name.
3. Select **Private**.
4. Leave **Add README**, **Add .gitignore** and **Choose a license** unselected; this package already supplies a README and ignore rules.
5. Click **Create repository** and copy its HTTPS repository URL.

Official guide: [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

## 2. Upload from your Mac

Extract the ZIP if needed. Use the `ai-engineer-nyc-2026` folder containing `README.md`, `outputs/` and `work/` as the repository root. Do not upload only the ZIP: people should be able to browse the individual files.

Open Terminal, type `cd ` (including the space), drag that folder into Terminal, and press Return. Then run these commands, replacing `YOUR-ACCOUNT` with your account or organization:

```sh
git init -b main
git add .
git commit -m "Add AI Engineer NYC 2026 conference knowledge archive"
git remote add origin https://github.com/YOUR-ACCOUNT/ai-engineer-nyc-2026.git
git push -u origin main
```

If prompted, complete GitHub authentication using your existing Git credential setup or GitHub Desktop. A GitHub account password is not a Git HTTPS credential. If you chose a different repository name, use the exact URL GitHub showed you. These instructions assume a new, empty remote repository.

Official guides: [Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) and [About authentication to GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).

## Alternative: GitHub Desktop

Create the empty repository on GitHub as above. In GitHub Desktop, sign in and choose **File → Clone repository**, then select it. Copy the **contents** of this package into the cloned folder. Review the changes, commit them to `main`, and choose **Push origin**.

This full archive contains more than 100 files, so Git/GitHub Desktop is easier than GitHub’s browser uploader, which accepts up to 100 files per upload. [Upload documentation](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## 3. Check the result

- Confirm that `README.md` appears on the repository’s home page.
- Confirm that `outputs/` contains ten final files and both distinct PowerPoint decks.
- Download/clone a fresh copy and open `START-HERE.html` locally.
- HTML reports run locally after downloading; GitHub’s normal file view displays their source.

Website hosting, GitHub Pages and public publication are separate from uploading this repository and are not configured by the package.
