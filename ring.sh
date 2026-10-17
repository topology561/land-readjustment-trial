#!/bin/bash
# 門鈴：叫醒另一端的排程。用法：bash /tmp/q/ring.sh issuer   或   bash /tmp/q/ring.sh executor
# 金鑰取自雲端環境之環境變數（ISSUER_FIRE_TOKEN／EXECUTOR_FIRE_TOKEN）；本腳本⛔ 印出金鑰。
# 輸出一列：RING <對象> http=<狀態碼> session=<新工作階段網址或空>
case "$1" in
  issuer)   ID=trig_01LJJucfgwSh8LfnQVg63aSr; TOKEN="$ISSUER_FIRE_TOKEN" ;;
  executor) ID=trig_015aMmeQfGhnxBSMKoSCyGxo; TOKEN="$EXECUTOR_FIRE_TOKEN" ;;
  *) echo "RING usage: ring.sh issuer|executor"; exit 2 ;;
esac
if [ -z "$TOKEN" ]; then echo "RING $1 http=none session= (環境變數未設·改待整點之排程)"; exit 3; fi
OUT=$(mktemp)
CODE=$(curl -sS -o "$OUT" -w '%{http_code}' -X POST \
  "https://api.anthropic.com/v1/claude_code/routines/$ID/fire" \
  -H "Authorization: Bearer $TOKEN" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{}' 2>/dev/null)
URL=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1])).get('claude_code_session_url',''))" "$OUT" 2>/dev/null)
rm -f "$OUT"
echo "RING $1 http=$CODE session=$URL"
[ "$CODE" = "200" ] && exit 0 || exit 1
