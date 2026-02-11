from function import log
from datetime import datetime
from pathlib import Path
import os


def init_folder():
    logger = log()
    now_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = Path(__file__).resolve().parent.parent
    root = base_dir / "backup" / now_time

    structure = {
        "info": {},
        "work": {
            "kitten": {},
            "kitten4": {},
            "kn": {},
            "coco": {},
            "turtle": {},
        },
        "forum": {"replied": {}},
        "library": {},
    }

    def create_dirs(base_path, tree):
        for name, subtree in tree.items():
            path = base_path / name
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"创建目录: {path}")
            create_dirs(path, subtree)

    root.mkdir(parents=True, exist_ok=True)
    create_dirs(root, structure)

    logger.info("创建备份文件夹完成")
    return True, now_time


def del_folder(path: str):
    logger = log()
    logger.info("正在删除空文件夹")
    if not os.path.isdir(path):
        return
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            logger.info(f"已删除：{full_path}")
            del_folder(full_path)
    if not os.listdir(path):
        os.rmdir(path)
    logger.info("删除空文件夹成功")
    return True
