import os
import re


def delete_all_sidebar(root_dir: str) -> None:
    for cur_dir, folds, files in os.walk(root_dir):
        for file in files:
            if file == '_sidebar.md':
                os.remove(os.path.join(cur_dir, file))


def auto_update_sidebar(root_dir: str) -> None:
    for curDir, folds, files in os.walk(root_dir):
        sidebarContent = list()
        if 'images' in curDir:
            continue
        if '1000_config' in curDir:
            continue

        if files:
            content = list()
            for file in files:
                if not file.endswith('.md'):
                    continue
                if file == '_sidebar.md':
                    continue
                if file == 'README.md':
                    continue

                file_dir = os.path.join(file).replace(
                    '\\', '/')
                content.append(f'  - [{file}]({file_dir})\n')

            if content:
                content.insert(0, '- files\n')
                sidebarContent.append(content)

        if folds:
            content = list()
            for fold in folds:
                if fold == 'images' or '1000' in fold:
                    continue
                fold_dir = os.path.join(
                    fold, '_sidebar.md').replace('\\', '/')
                content.append(f'  - [{fold}]({fold_dir})\n')

            if content:
                content.insert(0, '- folds\n')
                sidebarContent.append(content)

        title = curDir.split('_')[-1].removesuffix('.md')
        sidebarContent.insert(0, f'# {title}\n\n')

        with open(os.path.join(curDir, '_sidebar.md'), 'w', encoding='utf8') as f:
            for content in sidebarContent:
                f.writelines(content)


def auto_update_readme(root_dir: str) -> None:
    contents = list()
    for cur_dir, folds, files in os.walk(root_dir):
        for file in files:
            if file != '_sidebar.md':
                continue

            content = str()
            fold_name = cur_dir.split('\\')[-1]
            fold_id = fold_name.split('_')[0]
            id_len = len(fold_id)

            if id_len == 4:
                content += f'\n### {fold_name}\n\n'
                if '1010' in cur_dir:
                    file_path = cur_dir.split('10_note')[-1].replace('\\', '/')
                    content += f'- [{fold_name}](.{file_path}/_sidebar.md)\n'

            if id_len == 6:
                file_path = cur_dir.split('10_note')[-1].replace('\\', '/')
                content += f'- [{fold_name}](.{file_path}/_sidebar.md)\n'

            contents.append(content)

    with open(os.path.join(root_dir, 'README.md'), 'r', encoding='utf-8') as f:
        content = f.read()
        str_info = re.compile(r'目录[\s\S]*')
        contents = '目录\n'+''.join(contents)
        content_re = re.sub(str_info, contents, content)

    with open(os.path.join(root_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(content_re)


def auto_update_index(root_dir: str) -> None:
    contents = list()

    for cur_dir, folds, files in os.walk(root_dir):
        for file in files:
            if file == '_sidebar.md':
                continue
            if not file.endswith('md'):
                continue

            file_path = os.path.join(cur_dir, file).split(
                '10_note')[-1].replace('\\', '/')
            contents.append(file_path)

    contents = f'paths:{contents},'
    content_re = str()
    index_path = os.path.join(root_dir, 'index.html')

    with open(index_path, 'r', encoding='utf8') as f:
        content = f.read()
        str_info = re.compile(r'paths:\s\[[^\]]*\],')
        content_re = re.sub(str_info, contents, content)\

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content_re)


def print_valid_images(root_dir: str) -> list:
    images = list()
    for cur_dir, folds, files in os.walk(root_dir):

        for file in files:
            if not file.endswith('png'):
                continue
            images.append(os.path.join(cur_dir, file))

        cur_fold = cur_dir.split('\\')[-1]
        if cur_fold != 'images':
            continue

        parent_fold = os.path.dirname(cur_dir)
        parent_fold_files = os.listdir(parent_fold)
        md_files_path = list()

        for file in parent_fold_files:
            if not file.endswith('.md'):
                continue
            md_files_path.append(os.path.join(parent_fold, file))

        for path in md_files_path:
            content = str()
            with open(path, 'r', encoding='utf8') as f:
                content = f.read()
                for image in images[:]:
                    image_name = image.split('\\')[-1]
                    if image_name in content:
                        images.remove(image)

    for image in images:
        print(image)

    return images


def delete_valid_images(images: list) -> None:
    for image in images:
        os.remove(image)


def count_note_size(root_dir: str) -> None:
    size = 0
    num = 0

    for cur_dir, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.endswith('.md'):
                continue
            if file == '_sidebar.md':
                continue
            if file == 'README.md':
                continue

            size += os.path.getsize(os.path.join(cur_dir, file))
            num += 1

    print(f'共 {num} 个笔记')
    print(f'{size/(1024*1024)} MB')
    print(f'约合中文字符 {size/2} 个')


def find_long_note(root_dir: str) -> None:
    for cur_dir, folds, files in os.walk(root_dir):
        if 'diary' in cur_dir:
            continue

        for file in files:
            if not file.endswith('.md') or file == '_sidebar.md' or file == 'README.md' or '1020' in cur_dir:
                continue

            file_path = os.path.join(cur_dir, file)
            with open(file_path, 'r', encoding='utf8') as f:
                content = f.readlines()
                lines_num = len(content)

                if lines_num > 999:
                    print(file_path)


if __name__ == '__main__':
    dir = r'D:\kxh\10_note'

    delete_all_sidebar(dir)
    auto_update_sidebar(dir)
    auto_update_readme(dir)
    auto_update_index(dir)
    images = print_valid_images(dir)
    delete_valid_images(images)
    count_note_size(dir)
    find_long_note(dir)
