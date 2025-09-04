# testing-portfolio

个人测试/自动化作品集。每个项目都有独立目录，包含：目标、如何运行、主要结果与截图、CI 状态。

目录
- projects/api-tests - API 自动化示例（pytest + requests）
- projects/web-e2e - Web E2E 示例（Playwright / Selenium）
- projects/performance - 简单性能测试（locust/jmeter）
- exercises - 手工测试用例、设计样例

运行示例（在项目目录内）：
1. 创建虚拟环境： `python -m venv .venv`
2. 激活并安装依赖：
   - Windows: `.venv\Scripts\activate`
   - mac/linux: `source .venv/bin/activate`
   - `pip install -r requirements.txt`
3. 运行测试（pytest）： `pytest -q`
