### fetch data

#### need read

#### install
```bash
conda env create -f requirements.yml
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