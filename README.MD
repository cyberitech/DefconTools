# DefconTools
this repo is meant to hold a clone of tools presented at defcon.  While i attended some in the past, it was not until Defcon 31 I got the idea to do this.  Pull requests for tools released at other Defcons 
are welcome.  

Im going to be adding tools pegged to the commit hash according to the most recent hash at the time they were presented at Defcon.  If you want newer versions, you would need to update the individual package manually to the latest.

When submitting pull requests, please ensure the submodule is pegged to a release tag or commit hash that would have been used at that year's Defcon.

# Usage
Pull all tools at once (no existing repo)
```
git clone https://github.com/cyberitech/DefconTools --recursive
```
Pull all tools at once (existing repo)
```
git clone https://github.com/cyberitech/DefconTools
cd DefconTools
git submodule update --init --recursive
```
Pull only an individual tool (example: EvilnoVNC from Defcon 31, from the uncategorized folder)
```
git clone https://github.com/cyberitech/DefconTools
cd DefconTools
git submodule update --init "31/uncategorized/EvilnoVNC"
```
# Contributing
If you want to help add tools presented at Defcon on a given year, it takes about ~1 hour to do so.  Here are the steps:
1. Go to the Defcon page for your year.  URL for Defcon n is in format of `https://defcon.org/html/defcon-{n}/dc-{n}-index.html`
 * Example for Defcon 30: `https://defcon.org/html/defcon-30/dc-30-index.html`
 * Make a note of when the Defcon was... Defcon 30 ended on 2022 August 15, so make note of `2022-08-15`
2. Gather a list of all git repos you want to inlcude.
3. Clone this repo
 * `git clone https://github.com/cyberitech/DefconTools`
4. `cd` into the repo and make a directory for the defcon year `n`, and a subdirectory named `uncategorized`
 * `cd DefconTools && mkdir {n}/uncategorized`
5. Add each git repo as a submodule (idk lets try putting urls in a file named '/tmp/repos`)
 * `cd {n}/uncategorized && for while read line; do git submodule add $line; done < /tmp/repos`
6. Track the commit for each repo as presented at Defcon.  Go back to the root and run `hashfind.py {n} {date}`
 * Ex, defcon 30:  `python3 hashfind.py 30 2022-08-15`
7. Add and commit changes.  
 ` git add . && git commit -m "adding Defcon {n} tools`
8. Make a pull request
