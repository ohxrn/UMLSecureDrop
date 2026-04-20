#!/bin/bash

# ==== CHANGE THIS TO YOUR REAL main.py PATH ====
PROJECT_MAIN="/Users/jackohrn/code/UML/secureDrop/main.py"

# Create ~/bin if it doesn't exist
mkdir -p "$HOME/bin"

# Create the launcher script
cat > "$HOME/bin/secure_drop" <<EOF
#!/bin/bash
python3 "$PROJECT_MAIN" "\$@"
EOF

# Make the launcher executable
chmod +x "$HOME/bin/secure_drop"

# Add ~/bin to PATH in ~/.zshrc if it's not already there
if ! grep -q 'export PATH="$HOME/bin:$PATH"' "$HOME/.zshrc" 2>/dev/null; then
    echo '' >> "$HOME/.zshrc"
    echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.zshrc"
    echo 'Added ~/bin to PATH in ~/.zshrc'
else
    echo '~/bin already exists in PATH config'
fi

echo
echo 'Setup complete.'
echo 'Now run: source ~/.zshrc'
echo 'Then test with: which secure_drop'
echo 'And finally: secure_drop'