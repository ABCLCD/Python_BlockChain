# 导入模块，用来计算哈希值、获取时间
import hashlib
import datetime as date

# 定义区块结构
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # 一个区块包含的基本元素（索引，时间戳，数据，前一个区块的哈希值）
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    # 生成当前区块的哈希值
    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) +str(self.timestamp) +str(self.data) +str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

# 定义创世区块生成函数
def create_genesis_block():
    # index为0，时间为生成该区块的时间，数据填充为一个字符串，哈希值为0
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# 生成一个新的区块并添加到区块链中
def add_block_to_blockchain(blockchain, last_block):
    # 新区块各个要素的值
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    # 添加到链
    blockchain.append(Block(this_index, this_timestamp, this_data, this_hash))
    return blockchain


# 生成创世区块添加到链
blockchain = [create_genesis_block()]
# 前一个区块
previous_block = blockchain[0]
# 预设创世区块之后生成的区块数
num_of_blocks_to_add = 20
# 生成区块并添加到链
for i in range(0, num_of_blocks_to_add):
    blockchain = add_block_to_blockchain(blockchain, previous_block)
    previous_block = blockchain[-1]
    print( "Block #{} has been added to the blockchain!".format(previous_block.index) )
    print( "Hash: {}n".format(previous_block.hash) )