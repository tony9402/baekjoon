from typing import List, Optional

from baekjoon_utils.utils import get_api_result
from baekjoon_utils.docs.docs_types import (
    ContributorType,
)


def get_contributors() -> List[ContributorType]:
    url = "https://api.services.tony9402.com/contributor"
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }

    response = get_api_result(url=url, headers=headers)
    result = []
    for contributor in response["data"]:
        result.append(
            ContributorType.model_validate(contributor)
        )
    return result


def make_table(contributors: Optional[List[ContributorType]] = None) -> str:
    if contributors is None:
        contributors = get_contributors()

    res = []
    res.append("<table>")

    max_column = 5
    total_contributors = len(contributors)

    for batch_start_idx in range(0, total_contributors, max_column):
        batch = contributors[batch_start_idx:batch_start_idx+max_column]

        res.append(f"    <tr height=\"140px\">")
        # Contributor 이미지
        for contributor in batch:
            res.append(f"        <td align=\"center\" width=\"130px\">")
            github_url = f"https://github.com/{contributor.github_handle}"
            github_image_url = f"https://avatars.githubusercontent.com/u/{contributor.github_id}?v=4"
            github_image_component = f"<img height=\"100px\" width=\"100px\" src=\"{github_image_url}\"/>"
            component_with_image = f"<a href=\"{github_url}\">{github_image_component}</a>"
            component_with_name  = f"<a href=\"{github_url}\">{contributor.github_handle}</a>"
            res.append(f"            {component_with_image}")
            res.append(f"            <br />")
            res.append(f"            {component_with_name}")
            res.append(f"        </td>")
        res.append("    </tr>")

        # Contributor 정보
        res.append(f"    <tr height=\"50px\">")
        for contributor in batch:
            res.append("        <td align=\"center\">")
            if contributor.baekjoon_handle == "" or contributor.baekjoon_handle is None:
                res.append(f"            <b>private</b>")
            else:
                badge_component = f"<img src=\"http://mazassumnida.wtf/api/mini/generate_badge?boj={contributor.baekjoon_handle}\" />"
                boj_url_component = f"<a href=\"https://www.acmicpc.net/user/{contributor.baekjoon_handle}\">Baekjoon</a>"
                solved_url_component = f"<a href=\"https://solved.ac/profile/{contributor.baekjoon_handle}\">solved.ac</a>"
                res.append(f"            {badge_component}")
                res.append(f"            <br />")
                res.append(f"            {boj_url_component}")
                res.append(f"            <br />")
                res.append(f"            {solved_url_component}")
            res.append("        </td>")
        res.append("    </tr>")

    res.append("</table>")

    return "\n".join(res)

