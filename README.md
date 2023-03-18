
# Brute Force SSH
    This is a simple script to brute force SSH by Python for educational purpose
## Usage

```python
python3 brute_force_ssh <target> <port> <options>

-u      --usernanme              Username of remote host
-p      --password               Password of remote host
-uf     --userfile               Username filepath
-pf     --passfile               Password filepath
```

## Examples
Attacker machine: 192.168.72.130

Victim machine: 192.168.72.134

SSH port: 22

Remote user: kma2023-hvktmm2023

### Scenario 1: Attacking password
```python
python3 brute_force_ssh 192.168.72.134 22 -u kma2023 -uf passwords.txt
```

![App Screenshot](https://github.com/lelong2304/Brute-Force-SSH/blob/main/result_scenario_1.PNG)

### Scenario 2: Attacking username
```python
python3 brute_force_ssh 192.168.72.134 22 -u username.txt -p hvktmm2023
```

![App Screenshot](https://github.com/lelong2304/Brute-Force-SSH/blob/main/result_scenario_2.PNG)

### Scenario 3: Attacking both username and password
```python
python3 brute_force_ssh 192.168.72.134 22 -uf username.txt -pf passwords.txt
```

![App Screenshot](https://github.com/lelong2304/Brute-Force-SSH/blob/main/result_scenario_3.PNG)

## Reference
https://mohamedaezzat.github.io/posts/sshbruteforcer/