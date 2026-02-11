# CodemaoBackupMe
**说好从今以后都牵着手，因为要走很远 | 编程猫个人数据备份工具**

此项目正在开发，预计在三月前竣工。

本项目更多的是备份，因此存储的文件大部分为API直接的返回值（未经解析的JSON），你可以稍后使用其他工具解析。

除非特别标注，保存的文件均 `json` 格式

## 项目用途

不知道什么时候账号就被封了？不知道什么时候就被盗号了？不知道什么时候就被毁号了？没关系，你可以使用这个工具完整备份你在编程猫中留下的重要数据。并在需要时快速恢复

## 功能实现

**个人信息**

虽然备份了也恢复不回去了，但还请记得你是谁

- [ ] details/info（个人信息）
- [ ] honor（荣誉信息）
- [ ] work-list（作品列表）
- [ ] collect-list（收藏列表）
- [ ] followers-list（关注列表）
- [ ] fan-list（粉丝列表）

**作品**

备份所有作品，即使是未发布的

- [ ] works（完整作品信息）
- [ ] bcm（k3作品备份/源文件格式）
- [ ] bcm4（k4作品备份/源文件格式）
- [ ] coco（coco作品备份/源文件格式）
- [ ] bcmkn（KN作品备份/源文件格式）
- [ ] tur（turtle作品备份/源文件格式）
- [ ] reply（个人作品下所有评论）

**论坛**

发布的帖子，以及回复

- [ ] created（发布的帖子/HTML格式）
- [ ] reply（帖子回复/HTML格式）
- [ ] replied（自己发布的帖子回复/HTML格式）
  
**图书馆**

图书馆相关

- [ ] mynovel（个人发布的小说/HTML格式）
- [ ] info（小说信息/HTML格式）
- [ ] novelcollect（收藏的小说列表）

## 文件结构

```
{timestamp-folder}/
├── info/
│   ├── details.json
│   ├── info.json
│   ├── honor.json
│   ├── work-list.json
│   ├── collect-list.json
│   ├── followers-list.json
│   └── fan-list.json
│
├── work/
│   ├── kitten/
│   │   └── {作品名称}/
│   │       ├── {作品ID}.bcm
│   │       ├── info.json
│   │       └── reply.json
│   │
│   ├── kitten4/
│   │   └── {作品名称}/
│   │       ├── {作品ID}.bcm4
│   │       ├── info.json
│   │       └── reply.json
│   │
│   ├── kn/
│   │   └── {作品名称}/
│   │       ├── {作品ID}.bcmkn
│   │       ├── info.json
│   │       └── reply.json
│   │
│   ├── coco/
│   │   └── {作品名称}/
│   │       ├── {作品ID}.json
│   │       ├── info.json
│   │       └── reply.json
│   │
│   └── turtle/
│       └── {作品名称}/
│           ├── {作品ID}.tur
│           ├── info.json
│           └── reply.json
│
├── forum/
│   ├── {帖子ID-帖子标题}/
│   │   ├── post.html
│   │   └── reply/
│   │       └── {回帖ID-用户ID}.html
│   │
│   └── replied/
│       └── {帖子ID-帖子标题}/
│           └── {回帖ID}.html
│
└── library/
    ├── {小说ID-小说名}/
    │   ├── {章节名}.html
    │   └── info.html
    │
    └── novelcollect.json
```
