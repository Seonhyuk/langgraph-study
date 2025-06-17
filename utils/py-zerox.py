from pyzerox import zerox
import asyncio
import nest_asyncio

from dotenv import load_dotenv

nest_asyncio.apply()

load_dotenv()

kwargs = {}

custom_system_prompt = None

model = "gpt-4.1-mini"


async def main():
    file_path = "./documents/income_tax.pdf"

    select_pages = None

    output_dir = "./output_test"
    result = await zerox(
        file_path=file_path,
        model=model,
        output_dir=output_dir,
        custom_system_prompt=custom_system_prompt,
        select_pages=select_pages,
        **kwargs,
    )
    return result


result = asyncio.run(main())


print(result)
