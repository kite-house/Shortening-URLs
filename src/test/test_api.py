from httpx import AsyncClient

async def test_generate_slug(ac: AsyncClient):
    result = await ac.post('/cutback', json = {"url": 'https://its_test.com'})
