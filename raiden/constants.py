from enum import Enum

from eth_utils import to_canonical_address

from raiden_contracts.constants import (
    CONTRACT_ENDPOINT_REGISTRY,
    CONTRACT_SECRET_REGISTRY,
    CONTRACT_TOKEN_NETWORK_REGISTRY,
)


UINT64_MAX = 2 ** 64 - 1
UINT64_MIN = 0

INT64_MAX = 2 ** 63 - 1
INT64_MIN = -(2 ** 63)

UINT256_MAX = 2 ** 256 - 1


class EthClient(Enum):
    GETH = 1
    PARITY = 2
    TESTER = 3


# Deployed to Ropsten revival on 2018-07-09 from
# raiden-contracts@42ad67c10f82899c11dc4654c7daed2422f415aa
ROPSTEN_REGISTRY_ADDRESS = '0xDfD10bAe9CCC5EBf11bc6309A0645eFe9f979584'
ROPSTEN_DISCOVERY_ADDRESS = '0x81F7cC4F76Bf16a21a5d1ABfDfD1FB503E430368'
ROPSTEN_SECRET_REGISTRY_ADDRESS = '0xD1B506A716B50069Ac3C990e86253C645b61633D'

DISCOVERY_TX_GAS_LIMIT = 76000

ETH_RPC_DEFAULT_PORT = 8545
HTTP_PORT = 80
HTTPS_PORT = 443

EMPTY_HASH = bytes(32)
EMPTY_SIGNATURE = bytes(65)

START_QUERY_BLOCK_KEY = 'DefaultStartBlock'

MAINNET = 'mainnet'
ROPSTEN = 'ropsten'
RINKEBY = 'rinkeby'
KOVAN = 'kovan'
SMOKETEST = 'smoketest'

ID_TO_NETWORKNAME = {
    1: MAINNET,
    3: ROPSTEN,
    4: RINKEBY,
    42: KOVAN,
    627: SMOKETEST,
}

ID_TO_NETWORK_CONFIG = {
    3: {
        CONTRACT_ENDPOINT_REGISTRY: to_canonical_address(ROPSTEN_DISCOVERY_ADDRESS),
        CONTRACT_SECRET_REGISTRY: to_canonical_address(ROPSTEN_SECRET_REGISTRY_ADDRESS),
        CONTRACT_TOKEN_NETWORK_REGISTRY: to_canonical_address(ROPSTEN_REGISTRY_ADDRESS),
        START_QUERY_BLOCK_KEY: 3604000,  # 924 blocks before token network registry deployment
    },
}

NETWORKNAME_TO_ID = {
    name: id
    for id, name in ID_TO_NETWORKNAME.items()
}

MIN_REQUIRED_SOLC = 'v0.4.23'
NULL_ADDRESS = '0x' + '0' * 40
NULL_ADDRESS_BYTES = b'\x00' * 20

TESTNET_GASPRICE_MULTIPLIER = 2.0

GAS_REQUIRED_FOR_OPEN_CHANNEL = 111577
GAS_REQUIRED_FOR_SET_TOTAL_DEPOSIT = 44882
GAS_REQUIRED_FOR_REGISTER_SECRET = 46152
GAS_REQUIRED_FOR_CLOSE_CHANNEL = 113489
GAS_REQUIRED_FOR_BALANCE_PROOF = 94416
GAS_REQUIRED_FOR_SETTLE_CHANNEL = 105756
GAS_REQUIRED_FOR_UNLOCK_1_LOCKS = 44097
GAS_REQUIRED_FOR_UNLOCK_6_LOCKS = 83682
