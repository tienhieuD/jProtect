# jProtect

Using Cython to compile Odoo source code.

### Usage

Something like:

```shell script
> python3 ./jprotect-bin.py -fr <path_to_addons> -in <regex_1> <regex_2> -ex <regex_3> <regex_4>
``` 

- `-fr`, `--from_dir`: Folder contains list add-ons.
- `-to`, `--to_dir`: Folder to save after compile add-ons.
- `-in`, `--includes`: File path must include all regex.
- `-ex`, `--excludes`: File will be passed if include one of regex in list.
- `-nm`, `--name`: Name of project (optional).

For examples:

```shell script
python3 ./jprotect-bin.py -fr "D:\\myaddon\\tristar_project\\073.Odoo_TriStar\\trunk\\3. SourceCode\\addons" -in ".+?models.+?" ".+?tristar.+?" -ex ".+?__.py" ".+?tristar_payslip_sumary_canteen_foreign.py"
```

### Reference

- [Protecting Python Sources With Cython](https://medium.com/@xpl/protecting-python-sources-using-cython-dcd940bb188e)