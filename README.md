### fetch data

#### need read
```bash
python fetch_images.py
```

#### db setup
```
aerich init -t conf.db.TORTOISE_ORM
aerich init-db
```
- modify models
```
aerich migrate
aerich upgrade
```
- rewrite
```
aerich downgrade
aerich history
aerich heads
```