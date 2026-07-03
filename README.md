# Civ6ModAgent

## Project Description / 项目简介

### English Version
**Civ6ModAgent** is an experimental test project (updated irregularly) with the ultimate goal of empowering AI Agents to generate all necessary code files for a complete Civilization VI mod. 

> ⚠️ **Prerequisite**: Using this tool still requires a basic understanding of ModBuddy and Sid Meier's Civilization VI modding mechanics.

*Special thanks to **Hemmelfort** for their invaluable video tutorials, modding software, and documentation.*

**Current Progress:**
- Implementing simple unit tests
- Currently testing the building system
---

### 中文版本
**Civ6ModAgent** 是一个实验性的测试项目（不定期更新），最终目标是使 Agent 具备独立生成完整《文明6》模组所需全部代码文件的能力。

> ⚠️ **使用前提**：要成功制作和运行 Mod，您仍需对 ModBuddy 软件及《文明6》的基本模组机制有一定了解。

*特别鸣谢：**Hemmelfort**，感谢他提供的教学视频、开发软件和权威文档支持。*

**目前进度:**
- 实现简单的Unit的编写
- 正在进行Building的测试
---

## 🛠️ Integrated Skills & Tools / 已集成工具与技能

The agent utilizes a set of custom tools designed for Civilization VI modding:
1.  **`civ6_official_xml_query` & `civ6_base_game_dictionary_query`**: Queries official game data to retrieve template statistics and AI configurations.
2.  **`civ6_unit_creator`**: Automates unit creation by cloning template statistics and applying combat/moves/cost overrides.
3.  **`civ6_boilerplate_generator`**: Generates clean XML boilerplates for Leaders, Civilizations, and Buildings.
4.  **`civ6_localization_manager`**: Automatically synchronizes and manages translations (English & Simplified Chinese).
5.  **`civ6_modart_builder`**: Manages Mod.Art.xml dependency metadata and .artdef references.
