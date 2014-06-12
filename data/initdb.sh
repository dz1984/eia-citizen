if [ -f database.sqlite ]; then
	mv database.sqlite database.sqlite.old
fi

cat schema.sql | sqlite3 --header --column database.sqlite
python gen_eiadata.py

