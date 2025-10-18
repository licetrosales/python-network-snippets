# 1️⃣ Create and switch to the new branch
git checkout -b dev

# 2️⃣ Create a new file (e.g., datalink/protocol-f.py)
mkdir -p datalink
touch datalink/protocol-f.py

# 3️⃣ Add your code inside the file (example)
echo "# Protocol F - data link layer implementation" > datalink/protocol-f.py

# 4️⃣ Stage the file
git add datalink/protocol-f.py

# 5️⃣ Commit the change
git commit -m "feat(datalink): add protocol-f implementation"

# 6️⃣ Push the branch to remote
git push -u origin dev

## 🛠️ Pull Request Change Comparison

Comparing changes in PRs is a critical step in collaborative development.  
It allows the repository owner or reviewer to:

- ✅ Check for merge conflicts  
- 📝 Review proposed code changes  
- ✏️ Edit or refine any suggested modifications  

This ensures smooth integration and maintains codebase quality.

This step ensures code quality and maintains project stability during contributions.
