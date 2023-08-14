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
