fswatch -xnr -e ".*" -i ".md" ../serve/day | while read file event; do 
  echo $file $event
  python3 gen_html.py $file
  python3 gen_index.py
done
