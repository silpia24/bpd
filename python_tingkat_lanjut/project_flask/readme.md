1. install virtual environtment <br>
    `pip install virtualenv`

2. create new env <br>
    `virtualenv myenv`

3. active env
    - windows ` ./myenv/scripts/activate`
    - mac `source ./myenv/bin/activate`

4. if you got error permission denied then run command:
    - `Get-ExecutionPolicy`
    - `Get-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force`
