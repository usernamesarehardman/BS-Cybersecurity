# BS Cybersecurity - William Freeman

## Overview
This repository contains all coursework for my degree, organized by course prefix and number. Each course has its own directory, and assignments are managed using Git branches with sparse checkout for efficiency. There is a specific structre that I use for my repository for organization.

## Repository Structure
```
📁 Degree-Name/
├── 📁 Semester-Year/
│   ├── 📁 COURSE-Number/
│   │   ├── 📁 Assignment-Number/
│   │   │   ├── 📄 program_name.extension
│   │   │   ├── 📄 .gitignore
│   │   │   └── 📄 README.md   # Describe assignment
│   │   └── 📄 README.md       # Describe course
│   └── 📄 README.md           # Describe semester
├── 📄 .gitignore
├── 📄 LICENSE
└── 📄 README.md
```

## How to Use Git Branches for Assignments
### **Create a New Branch for an Assignment**
1. Switch to the main branch and ensure it's up to date:
   ```sh
   git checkout main
   git pull origin main
   ```
2. Create a new branch for an assignment:
   ```sh
   git checkout -b COURSE-Number/Assignment-Number
   ```
3. Work on the assignment, then commit changes:
   ```sh
   git add COURSE-Number/Assignment-Number/
   git commit -m "Completed COURSE-Number Assignment-Number"
   ```
4. Push the new branch to GitHub:
   ```sh
   git push origin COURSE-Number/Assignment-Number
   ```
5. When done, merge it back into `main`:
   ```sh
   git checkout main
   git merge COURSE-Number/Assignment-Number
   git push origin main
   ```

## How to Use Sparse Checkout to Work on One Course at a Time
Sparse checkout lets you clone only a specific course folder instead of downloading everything.

### **Enable Sparse Checkout**
1. Clone the repository without files:
   ```sh
   git clone --no-checkout https://github.com/usernamesarehardman/Degree-Name.git
   cd Degree-Name
   ```
2. Enable sparse checkout mode:
   ```sh
   git sparse-checkout init --cone
   ```
3. Specify the course folder you want to work on:
   ```sh
   git sparse-checkout set COURSE-Number
   ```
4. Pull only that folder:
   ```sh
   git checkout main
   ```

### **Switching to a Different Course**
To change the folder you are working on, update sparse checkout:
```sh
git sparse-checkout set COURSE-Number/Assignment-Number
```

## License
This repository is licensed under the MIT License. See `LICENSE` for details.

## Author
**William Freeman**  
[GitHub](https://github.com/usernamesarehardman) | 
[LinkedIn](https://www.linkedin.com/in/william-freeman-2605411b1/) | 
[Bluesky](https://bsky.app/profile/usernamesarehardyo.bsky.social)