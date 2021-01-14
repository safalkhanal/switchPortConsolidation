# Switch port Consolidation
This project is the collection of PyATS test scripts to migrate source switch port to target switch port

## Requirement

Need to install the following modules

```bash
pip3 install pyats
pip3 install genie
pip3 install pyats.contrib
```

## Execution
To run the project, run the gui.py file
```bash
python gui.py
```
## Testbed sample file
hostname | ip | username | password | protocol | os |
--- | --- | --- | --- |--- |--- |
Switch1 | 192.168.1.1:32576 | cisco | cisco | telnet | ios | 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)