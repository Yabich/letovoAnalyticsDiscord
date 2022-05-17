import asyncio
import logging as log
import time
import aiohttp
import utils.errors as errors


class API:
    def __init__(self, session):
        self.session = session

    async def receive_token(
            self, login,
            password
    ):
        login_data = {
            "login": login,
            "password": password
        }
        async with self.session.post(url="https://s-api.letovo.ru/api/login", data=login_data) as resp:
            if resp.status != 200:
                raise errors.NotAuthorized(resp.status_code)
            resp_j = await resp.json()
            return f'{resp_j["data"]["token_type"]} {resp_j["data"]["token"]}'

    async def receive_student_id(
            self, token
    ) -> int:

        headers = {
            "Authorization": token
        }
        try:
            async with self.session.post(url="https://s-api.letovo.ru/api/me", headers=headers) as resp:
                if resp.status != 200:
                    print(f"Cannot get data from s.letovo.ru. Error {resp.status}")
                resp_j = await resp.json()
                return int(resp_j["data"]["user"]["student_id"])
        except aiohttp.ClientConnectionError:
            raise aiohttp.ClientConnectionError("Cannot establish connection to s.letovo.ru")
    #
    # async def receive_hw_n_schedule(
    #         self, sender_id: str, fs: CredentialsDatabase
    # ) -> bytes:
    #     student_id, token = await asyncio.gather(
    #         fs.get_student_id(sender_id=sender_id),
    #         fs.get_token(sender_id=sender_id)
    #     )
    #     if errors_l.NothingFoundError in (student_id, token):
    #         raise errors_l.NothingFoundError("Nothing found in the database for this user")
    #
    #     url = (
    #         f"https://s-api.letovo.ru/api/schedule/{student_id}/week?schedule_date="
    #         f"{time.strftime('%Y-%m-%d')}"
    #     )
    #     headers = {
    #         "Authorization": token,
    #     }
    #
    #     try:
    #         async with self.session.get(url=url, headers=headers) as resp:
    #             if resp.status != 200:
    #                 raise errors_l.UnauthorizedError(f"Cannot get data from s.letovo.ru. Error {resp.status}")
    #             return await resp.content.read()
    #     except aiohttp.ClientConnectionError as err:
    #         log.error(err)
    #         raise aiohttp.ClientConnectionError("Cannot establish connection to s.letovo.ru")
    #
    async def receive_marks(
            self, student_id, token
    ) -> bytes:
        url = f"https://s-api.letovo.ru/api/schoolprogress/{student_id}?period_num="
        if int(time.strftime("%m")) >= 9:
            url += "1"
        else:
            url += "2"

        headers = {
            "Authorization": token,
        }

        try:
            async with self.session.get(url=url, headers=headers) as resp:
                if resp.status != 200:
                    raise errors.UnauthorizedError(f"Cannot get data from s.letovo.ru. Error {resp.status}")
                return await resp.json()
        except aiohttp.ClientConnectionError as err:
            log.error(err)
            raise aiohttp.ClientConnectionError("Cannot establish connection to s.letovo.ru")
