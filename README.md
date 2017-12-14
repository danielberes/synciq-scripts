# SyncIQ-Scripts
Various scripts to use the SyncIQ local library

---

Currently tested on OneFS Versions:

* 7.1.1.4
* 7.1.1.8
* 7.2.0.1
* 7.2.1.1
* 8.0.0.0 (planned)

### How does it work
```
cl2-7114-1# python ./delete_synciq_file.py  --policy Sub-Minor --file /ifs/data/backup-clusterOne/file77,/ifs/data/backup-clusterOne/file72

Starting process...

SUCCESS: Deleted /ifs/data/backup-clusterOne/file77
SUCCESS: Deleted /ifs/data/backup-clusterOne/file72

Ending process.

cl2-7114-1#
```
### If there is an error
```
cl2-7114-1# python ./delete_synciq_file.py  --policy Sub-Minor --file /ifs/data/backup-clusterOne/file69,/ifs/data/backup-clusterOne/file67

Starting process...

FAILURE: Cannot delete /ifs/data/backup-clusterOne/file69.
FAILURE: Cannot delete /ifs/data/backup-clusterOne/file67.

There were 2 error(s).

Ending process.

cl2-7114-1#
```
