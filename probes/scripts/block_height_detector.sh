start=$(./cmc query block-by-height --chain-id=chain1 --sdk-conf-path=./testdata/sdk_config.yml | jq '.block.header.block_height')
sleep 900
end=$(./cmc query block-by-height --chain-id=chain1 --sdk-conf-path=./testdata/sdk_config.yml | jq '.block.header.block_height')
if [ "$start" -ne "$end" ]; then
        echo true
else
        echo false
fi
