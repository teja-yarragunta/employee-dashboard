import {
  Box,
  Button,
  Container,
  Flex,
  Text,
  useColorMode,
  useColorModeValue,
} from "@chakra-ui/react";
import { IoMoon } from "react-icons/io5";
import { LuSun } from "react-icons/lu";
import { color } from "framer-motion";
import React from "react";
import CreateUserModel from "./CreateUserModel";

const Navbar = ({ setUsers }) => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Container maxW={"1000px"}>
      <Box
        px={5}
        my={5}
        borderRadius={5}
        bg={useColorModeValue("gray.200", "gray.700")}
      >
        <Flex h="16" alignItems={"center"} justifyContent={"space-between"}>
          {/* left side */}
          <Flex alignItems={"center"} justifyContent={"center"} gap={3}>
            <Text
              fontSize={{ base: "18px", sm: "24px", md: "40px" }}
              fontWeight="bold"
              whiteSpace="nowrap"
              overflow="hidden"
              textOverflow="ellipsis"
            >
              Employee Dashboard
            </Text>
          </Flex>
          {/* right side */}
          <Flex gap={3} alignItems={"center"}>
            <Text
              fontSize={"lg"}
              fontWeight={500}
              display={{ base: "none", md: "block" }}
            >
              OnePiece Company
            </Text>
            <Button onClick={toggleColorMode}>
              {colorMode === "light" ? <IoMoon /> : <LuSun size={20} />}
            </Button>
            <CreateUserModel setUsers={setUsers} />
          </Flex>
        </Flex>
      </Box>
    </Container>
  );
};

export default Navbar;
