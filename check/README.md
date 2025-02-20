# 博客检测程序

这个文件夹包含了用于检测博客可访问性的相关文件：

- `check_blogs.py`: 博客可访问性检测程序
- `inaccessible_blogs.csv`: 当前无法访问的博客列表

## 使用方法

运行以下命令来检测博客的可访问性：

```bash
python3 check_blogs.py
```

程序会自动检查 `inaccessible_blogs.csv` 中的博客是否恢复可访问。如果恢复可访问，会将其移回到主目录下的 `blogs-list.csv` 中。