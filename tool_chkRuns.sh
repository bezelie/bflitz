# check running programs
echo "--- shell -----------------------"
ps aux | grep sh | grep -v grep
echo
echo "--- julius ---------------------"
ps aux | grep julius | grep -v grep
echo
echo "--- python ---------------------"
ps aux | grep python | grep -v grep

