# mycalc — 超迷你數學函式庫 🧮

示範專案結構、依賴安裝與 Pytest 測試。
在 Codex Cloud or GitHub Actions 上可一鍵跑完 CI。

## 使用方式

```bash
pip install -r requirements.txt
python -c "from mycalc import add, mul, sub, div; print(add(1, 2), mul(3, 4), sub(5, 1), div(8, 2))"
pytest
```
