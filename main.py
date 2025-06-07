import asyncio
import argparse
from pathlib import Path
from aiofile import async_open
import os
from logger import logger


async def read_folder(source_folder: Path, output_folder: Path):
    tasks = []
    
    try:
        for item in source_folder.rglob('*'):
            if item.is_file():
                task = copy_file(item, output_folder)
                tasks.append(task)
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
            
    except Exception as e:
        logger.error(f"Error reading folder {source_folder}: {e}")


async def copy_file(file_path: Path, output_folder: Path):
    try:
        extension = file_path.suffix[1:].lower() if file_path.suffix else 'no_extension'
        
        target_dir = output_folder / extension
        os.makedirs(target_dir, exist_ok=True)
        
        target_file = target_dir / file_path.name
        
        counter = 1
        original_target = target_file
        while target_file.exists():
            stem = original_target.stem
            suffix = original_target.suffix
            target_file = target_dir / f"{stem}_{counter}{suffix}"
            counter += 1
        
        async with async_open(file_path, 'rb') as src:
            async with async_open(target_file, 'wb') as dst:
                content = await src.read()
                await dst.write(content)
        
        logger.info(f"Copied {file_path} to {target_file}")
        
    except Exception as e:
        logger.error(f"Error copying file {file_path}: {e}")


async def main():
    parser = argparse.ArgumentParser(description='Asynchronously sort files by extension')
    parser.add_argument('source', help='Source folder path')
    parser.add_argument('output', help='Output folder path')
    
    args = parser.parse_args()
    
    source_folder = Path(args.source)
    output_folder = Path(args.output)
    
    if not source_folder.exists():
        logger.error(f"Source folder {source_folder} does not exist")
        return
    
    if not source_folder.is_dir():
        logger.error(f"Source path {source_folder} is not a directory")
        return
    
    try:
        os.makedirs(output_folder, exist_ok=True)
    except Exception as e:
        logger.error(f"Error creating output folder {output_folder}: {e}")
        return
    
    logger.info(f"Starting file sorting from {source_folder} to {output_folder}")
    
    await read_folder(source_folder, output_folder)
    
    logger.info("File sorting completed")


if __name__ == "__main__":
    asyncio.run(main())
