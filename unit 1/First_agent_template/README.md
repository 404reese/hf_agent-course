---
title: First Agent Template
emoji: ⚡
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 5.23.1
app_file: app.py
pinned: false
tags:
- smolagents
- agent
- smolagent
- tool
- agent-course
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


prompts to try :

Who won the FIFA World Cup in 2022?
What time is it in Tokyo?
= Agent:
Calls
get_current_time_in_timezone("Asia/Tokyo")
Returns current time

3. Generate images

User:

Generate a cyberpunk cat riding a motorcycle

Agent:

Calls image_generation_tool
Creates image