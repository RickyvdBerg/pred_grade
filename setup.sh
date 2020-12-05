mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"ra.vandenberg1@student.avans.nl\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\