# ip地址无效话
class Solution:
    def defangIPaddr(self, address: str) -> str:
        splits = address.split(".")
        return str.join('[.]', splits)

    def defangIPaddrOfReplact(self, address):
        return address.replace(".", "[.]")
