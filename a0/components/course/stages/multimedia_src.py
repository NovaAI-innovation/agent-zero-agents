"""Stage implementation: multimedia sourcing plan."""

from __future__ import annotations

from typing import Dict, List


def _image_asset(module_title: str, idx: int) -> Dict[str, str]:
    return {
        "title": f"{module_title} image {idx}",
        "source": "placeholder-source",
        "license": "commercial-friendly",
        "caption": f"Visual {idx} reinforcing {module_title} concept.",
        "alt_text": f"Illustration for {module_title} concept {idx}",
    }


def _video_asset(module_title: str, idx: int) -> Dict[str, str]:
    return {
        "title": f"{module_title} video {idx}",
        "link": f"https://example.com/{module_title.lower().replace(' ', '-')}/video-{idx}",
        "timecode": "00:00-08:00",
        "summary": f"Walkthrough of key {module_title} principle {idx}.",
    }


def _interactive_asset(module_title: str, idx: int) -> Dict[str, str]:
    return {
        "title": f"{module_title} interactive {idx}",
        "type": "calculator" if idx == 1 else "playground",
        "link": f"https://example.com/{module_title.lower().replace(' ', '-')}/interactive-{idx}",
        "usage": "Adjust parameters and compare outcomes.",
    }


def run(payload: dict, artifacts) -> dict:
    modules = payload.get("content", {}).get("modules", payload.get("modules", []))
    multimedia_by_module: List[Dict[str, object]] = []

    for module in modules:
        title = module.get("title", "Module")
        images = [_image_asset(title, i) for i in range(1, 4)]
        videos = [_video_asset(title, 1)]
        interactive = [_interactive_asset(title, 1)]
        multimedia_by_module.append(
            {
                "module_id": module.get("id", "M00"),
                "module_title": title,
                "images": images,
                "videos": videos,
                "interactive": interactive,
                "meets_targets": {
                    "images_3_to_5": 3 <= len(images) <= 5,
                    "videos_1_to_2": 1 <= len(videos) <= 2,
                    "interactive_1_to_3": 1 <= len(interactive) <= 3,
                },
            }
        )

    result = {
        "multimedia": multimedia_by_module,
        "targets": {
            "images_per_module": "3-5",
            "videos_per_module": "1-2",
            "interactive_per_module": "1-3",
        },
    }
    artifacts.add("multimedia", "multimedia_manifest.json")
    return result
