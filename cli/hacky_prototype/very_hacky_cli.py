# Copyright (c) 2022 MobileCoin, Inc.

import asyncio
from inspect import ArgSpec
import aiohttp
import json
import logging
import base64
from typing import Optional
import ssl
#import forest_utils as utils
import aiocmd

# IGNORE ME, I AM VERY BAD AND SHOULD BE IGNORED 
# but i *kind of* work just fine :))

# if not utils.get_secret("ROOTCRT"):
#     ssl_context: Optional[ssl.SSLContext] = None
# else:
#     ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#     root = open("rootcrt.pem", "wb")
#     root.write(base64.b64decode(utils.get_secret("ROOTCRT")))
#     root.flush()
#     client = open("client.full.pem", "wb")
#     client.write(base64.b64decode(utils.get_secret("CLIENTCRT")))
#     client.flush()

#     ssl_context.load_verify_locations("rootcrt.pem")
#     ssl_context.verify_mode = ssl.CERT_REQUIRED
#     ssl_context.load_cert_chain(certfile="client.full.pem")


class Request:
    url = 'http://localhost:9090/wallet/v2'        
    async def req(self, request_data: dict) -> dict:
        logging.info("request: %s", request_data.get("method"))
        request_data['params'] = {k:v for k,v in request_data['params'].items() if v} # handle optional arguments 
        response_data = await self.request(request_data)
        if "error" in str(response_data):
            logging.error(response_data)
        else:
            print(response_data)
        return response_data

    async def request(self, request_data: dict):
        #self.request_count += 1
        request_data = {"jsonrpc": "2.0", "id": '1', **request_data}
        print(f"request data: {request_data}")
        async with aiohttp.TCPConnector() as conn:
            async with aiohttp.ClientSession(connector=conn) as sess:
                # this can hang (forever?) if there's no full-service at that url
                async with sess.post(
                    self.url,
                    data=json.dumps(request_data),
                    headers={"Content-Type": "application/json"},
                ) as resp:
                    #print(resp.json)
                    return await resp.json()


class FullServiceAPIv2(Request, aiocmd.PromptToolkitCmd):
	async def do_assign_address_for_account(self, account_id, metadata=""):
		return await self.req(
			{
				"method": "assign_address_for_account",
				"params": {"account_id": account_id, "metadata": metadata},
			}
		)


	async def do_build_and_submit_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
		comment="",
	):
		return await self.req(
			{
				"method": "build_and_submit_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
					"comment": comment,
				},
			}
		)

	


	async def do_build_burn_transaction(
		self,
		account_id,
		amount={"value": "", "token_id": ""},
		redemption_memo_hex="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_burn_transaction",
				"params": {
					"account_id": account_id,
					"amount": amount,
					"redemption_memo_hex": redemption_memo_hex,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def do_build_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def do_build_unsigned_burn_transaction(
		self,
		account_id,
		amount={"value": "", "token_id": ""},
		redemption_memo_hex="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_unsigned_burn_transaction",
				"params": {
					"account_id": account_id,
					"amount": amount,
					"redemption_memo_hex": redemption_memo_hex,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def do_build_unsigned_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_unsigned_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def do_create_payment_request(
		self, account_id, subaddress_index="", amount={"value": "", "token_id": ""}, memo=""
	):
		return await self.req(
			{
				"method": "create_payment_request",
				"params": {
					"account_id": account_id,
					"subaddress_index": subaddress_index,
					"amount": amount,
					"memo": memo,
				},
			}
		)


	async def do_create_view_only_account_import_request(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "create_view_only_account_import_request",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def do_create_view_only_account_sync_request(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "create_view_only_account_sync_request",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def do_export_account_secrets(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "export_account_secrets",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def do_get_account_status(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "get_account_status",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def do_get_address_for_account(self, account_id, index=""):
		return await self.req(
			{
				"method": "get_address_for_account",
				"params": {"account_id": account_id, "index": index},
			}
		)


	async def do_get_addresses(self, account_id, offset="", limit=""):
		return await self.req(
			{
				"method": "get_addresses",
				"params": {"account_id": account_id, "offset": offset, "limit": limit},
			}
		)


	async def do_get_transaction_logs(
		self, account_id, min_block_index="", max_block_index="", offset="", limit=""
	):
		return await self.req(
			{
				"method": "get_transaction_logs",
				"params": {
					"account_id": account_id,
					"min_block_index": min_block_index,
					"max_block_index": max_block_index,
					"offset": offset,
					"limit": limit,
				},
			}
		)


	async def do_get_txos(
		self,
		account_id,
		address="",
		status="",
		token_id="",
		min_received_block_index="",
		max_received_block_index="",
		offset="",
		limit="",
	):
		return await self.req(
			{
				"method": "get_txos",
				"params": {
					"account_id": account_id,
					"address": address,
					"status": status,
					"token_id": token_id,
					"min_received_block_index": min_received_block_index,
					"max_received_block_index": max_received_block_index,
					"offset": offset,
					"limit": limit,
				},
			}
		)


	async def do_remove_account(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "remove_account",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def do_sync_view_only_account(
		self, account_id, completed_txos="", next_subaddress_index=""
	):
		return await self.req(
			{
				"method": "sync_view_only_account",
				"params": {
					"account_id": account_id,
					"completed_txos": completed_txos,
					"next_subaddress_index": next_subaddress_index,
				},
			}
		)


	async def do_update_account_name(self, account_id, name=""):
		return await self.req(
			{
				"method": "update_account_name",
				"params": {"account_id": account_id, "name": name},
			}
		)


	async def do_validate_confirmation(self, account_id, txo_id="", confirmation=""):
		return await self.req(
			{
				"method": "validate_confirmation",
				"params": {
					"account_id": account_id,
					"txo_id": txo_id,
					"confirmation": confirmation,
				},
			}
		)


	async def do_get_network_status(self):
		return await self.req({"method": "get_network_status"})


	async def do_get_wallet_status(self):
		return await self.req({"method": "get_wallet_status"})


	async def do_version(self):
		return await self.req({"method": "version"})


	async def do_check_b58_type(self, b58_code=""):
		return await self.req(
			{"method": "check_b58_type", "params": {"b58_code": b58_code}}
		)


	async def do_check_receiver_receipt_status(
		self,
		address="",
		receiver_receipt={
			"public_key": "",
			"confirmation": "",
			"tombstone_block": "",
			"amount": {
				"commitment": "",
				"masked_value": "",
				"masked_token_id": "",
				"version": "V1",
			},
		},
	):
		return await self.req(
			{
				"method": "check_receiver_receipt_status",
				"params": {"address": address, "receiver_receipt": receiver_receipt},
			}
		)


	async def do_create_account(self, name=""):
		return await self.req(
			{"method": "create_account", "params": {"name": name}}
		)


	async def do_create_receiver_receipts(
		self,
		tx_proposal={
			"input_txos": [],
			"payload_txos": [],
			"change_txos": [],
			"fee_amount": {"value": "", "token_id": ""},
			"tombstone_block_index": "",
			"tx_proto": "",
		},
	):
		return await self.req(
			{"method": "create_receiver_receipts", "params": {"tx_proposal": tx_proposal}}
		)


	async def do_get_accounts(self, offset="", limit=""):
		return await self.req(
			{"method": "get_accounts", "params": {"offset": offset, "limit": limit}}
		)


	async def do_get_address(self, public_address_b58=""):
		return await self.req(
			{"method": "get_address", "params": {"public_address_b58": public_address_b58}}
		)


	async def do_get_address_status(self, address=""):
		return await self.req(
			{"method": "get_address_status", "params": {"address": address}}
		)


	async def do_get_block(self, block_index=""):
		return await self.req(
			{"method": "get_block", "params": {"block_index": block_index}}
		)


	async def do_get_confirmations(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_confirmations",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def do_get_mc_protocol_transaction(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_mc_protocol_transaction",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def do_get_mc_protocol_txo(self, txo_id=""):
		return await self.req(
			{"method": "get_mc_protocol_txo", "params": {"txo_id": txo_id}}
		)


	async def do_get_transaction_log(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_transaction_log",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def do_get_txo(self, txo_id=""):
		return await self.req({"method": "get_txo", "params": {"txo_id": txo_id}})


	async def do_get_txo_block_index(self, public_key=""):
		return await self.req(
			{"method": "get_txo_block_index", "params": {"public_key": public_key}}
		)


	async def do_get_txo_membership_proofs(self, outputs=""):
		return await self.req(
			{"method": "get_txo_membership_proofs", "params": {"outputs": outputs}}
		)


	async def do_import_account(
		self,
		mnemonic="",
		key_derivation_version="",
		name="",
		first_block_index="",
		next_subaddress_index="",
		fog_info="",
	):
		return await self.req(
			{
				"method": "import_account",
				"params": {
					"mnemonic": mnemonic,
					"key_derivation_version": key_derivation_version,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
					"fog_info": fog_info,
				},
			}
		)


	async def do_import_account_from_legacy_root_entropy(
		self,
		entropy="",
		name="",
		first_block_index="",
		next_subaddress_index="",
		fog_info="",
	):
		return await self.req(
			{
				"method": "import_account_from_legacy_root_entropy",
				"params": {
					"entropy": entropy,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
					"fog_info": fog_info,
				},
			}
		)


	async def do_import_view_only_account(
		self,
		view_private_key="",
		spend_public_key="",
		name="",
		first_block_index="",
		next_subaddress_index="",
	):
		return await self.req(
			{
				"method": "import_view_only_account",
				"params": {
					"view_private_key": view_private_key,
					"spend_public_key": spend_public_key,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
				},
			}
		)


	async def do_sample_mixins(self, num_mixins="", excluded_outputs=""):
		return await self.req(
			{
				"method": "sample_mixins",
				"params": {"num_mixins": num_mixins, "excluded_outputs": excluded_outputs},
			}
		)


	async def do_submit_transaction(
		self,
		tx_proposal={
			"input_txos": [],
			"payload_txos": [],
			"change_txos": [],
			"fee_amount": {"value": "", "token_id": ""},
			"tombstone_block_index": "",
			"tx_proto": "",
		},
		comment="",
		account_id="",
	):
		return await self.req(
			{
				"method": "submit_transaction",
				"params": {
					"tx_proposal": tx_proposal,
					"comment": comment,
					"account_id": account_id,
				},
			}
		)


	async def do_verify_address(self, address=""):
		return await self.req({"method": "verify_address", "params": {"address": address}})


class FullServiceAPIv1(Request):
	async def assign_address_for_account(self, account_id, metadata=""):
		return await self.req(
			{
				"method": "assign_address_for_account",
				"params": {"account_id": account_id, "metadata": metadata},
			}
		)


	async def build_and_submit_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
		comment="",
	):
		return await self.req(
			{
				"method": "build_and_submit_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
					"comment": comment,
				},
			}
		)


	async def build_burn_transaction(
		self,
		account_id,
		amount={"value": "", "token_id": ""},
		redemption_memo_hex="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_burn_transaction",
				"params": {
					"account_id": account_id,
					"amount": amount,
					"redemption_memo_hex": redemption_memo_hex,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def build_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def build_unsigned_burn_transaction(
		self,
		account_id,
		amount={"value": "", "token_id": ""},
		redemption_memo_hex="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_unsigned_burn_transaction",
				"params": {
					"account_id": account_id,
					"amount": amount,
					"redemption_memo_hex": redemption_memo_hex,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def build_unsigned_transaction(
		self,
		account_id,
		addresses_and_amounts="",
		recipient_public_address="",
		amount="",
		input_txo_ids="",
		fee_value="",
		fee_token_id="",
		tombstone_block="",
		max_spendable_value="",
	):
		return await self.req(
			{
				"method": "build_unsigned_transaction",
				"params": {
					"account_id": account_id,
					"addresses_and_amounts": addresses_and_amounts,
					"recipient_public_address": recipient_public_address,
					"amount": amount,
					"input_txo_ids": input_txo_ids,
					"fee_value": fee_value,
					"fee_token_id": fee_token_id,
					"tombstone_block": tombstone_block,
					"max_spendable_value": max_spendable_value,
				},
			}
		)


	async def create_payment_request(
		self, account_id, subaddress_index="", amount={"value": "", "token_id": ""}, memo=""
	):
		return await self.req(
			{
				"method": "create_payment_request",
				"params": {
					"account_id": account_id,
					"subaddress_index": subaddress_index,
					"amount": amount,
					"memo": memo,
				},
			}
		)


	async def create_view_only_account_import_request(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "create_view_only_account_import_request",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def create_view_only_account_sync_request(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "create_view_only_account_sync_request",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def export_account_secrets(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "export_account_secrets",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def get_account_status(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "get_account_status",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def get_address_for_account(self, account_id, index=""):
		return await self.req(
			{
				"method": "get_address_for_account",
				"params": {"account_id": account_id, "index": index},
			}
		)


	async def get_addresses(self, account_id, offset="", limit=""):
		return await self.req(
			{
				"method": "get_addresses",
				"params": {"account_id": account_id, "offset": offset, "limit": limit},
			}
		)


	async def get_transaction_logs(
		self, account_id, min_block_index="", max_block_index="", offset="", limit=""
	):
		return await self.req(
			{
				"method": "get_transaction_logs",
				"params": {
					"account_id": account_id,
					"min_block_index": min_block_index,
					"max_block_index": max_block_index,
					"offset": offset,
					"limit": limit,
				},
			}
		)


	async def get_txos(
		self,
		account_id,
		address="",
		status="",
		token_id="",
		min_received_block_index="",
		max_received_block_index="",
		offset="",
		limit="",
	):
		return await self.req(
			{
				"method": "get_txos",
				"params": {
					"account_id": account_id,
					"address": address,
					"status": status,
					"token_id": token_id,
					"min_received_block_index": min_received_block_index,
					"max_received_block_index": max_received_block_index,
					"offset": offset,
					"limit": limit,
				},
			}
		)


	async def remove_account(
		self,
		account_id,
	):
		return await self.req(
			{
				"method": "remove_account",
				"params": {
					"account_id": account_id,
				},
			}
		)


	async def sync_view_only_account(
		self, account_id, completed_txos="", next_subaddress_index=""
	):
		return await self.req(
			{
				"method": "sync_view_only_account",
				"params": {
					"account_id": account_id,
					"completed_txos": completed_txos,
					"next_subaddress_index": next_subaddress_index,
				},
			}
		)


	async def update_account_name(self, account_id, name=""):
		return await self.req(
			{
				"method": "update_account_name",
				"params": {"account_id": account_id, "name": name},
			}
		)


	async def validate_confirmation(self, account_id, txo_id="", confirmation=""):
		return await self.req(
			{
				"method": "validate_confirmation",
				"params": {
					"account_id": account_id,
					"txo_id": txo_id,
					"confirmation": confirmation,
				},
			}
		)


	async def get_network_status(self):
		return await self.req({"method": "get_network_status"})


	async def get_wallet_status(self):
		return await self.req({"method": "get_wallet_status"})


	async def version(self):
		return await self.req({"method": "version"})


	async def check_b58_type(self, b58_code=""):
		return await self.req(
			{"method": "check_b58_type", "params": {"b58_code": b58_code}}
		)


	async def check_receiver_receipt_status(
		self,
		address="",
		receiver_receipt={
			"public_key": "",
			"confirmation": "",
			"tombstone_block": "",
			"amount": {
				"commitment": "",
				"masked_value": "",
				"masked_token_id": "",
				"version": "V1",
			},
		},
	):
		return await self.req(
			{
				"method": "check_receiver_receipt_status",
				"params": {"address": address, "receiver_receipt": receiver_receipt},
			}
		)


	async def create_account(self, name="", fog_info=""):
		return await self.req(
			{"method": "create_account", "params": {"name": name, "fog_info": fog_info}}
		)


	async def create_receiver_receipts(
		self,
		tx_proposal={
			"input_txos": [],
			"payload_txos": [],
			"change_txos": [],
			"fee_amount": {"value": "", "token_id": ""},
			"tombstone_block_index": "",
			"tx_proto": "",
		},
	):
		return await self.req(
			{"method": "create_receiver_receipts", "params": {"tx_proposal": tx_proposal}}
		)


	async def get_accounts(self, offset="", limit=""):
		return await self.req(
			{"method": "get_accounts", "params": {"offset": offset, "limit": limit}}
		)


	async def get_address(self, public_address_b58=""):
		return await self.req(
			{"method": "get_address", "params": {"public_address_b58": public_address_b58}}
		)


	async def get_address_status(self, address=""):
		return await self.req(
			{"method": "get_address_status", "params": {"address": address}}
		)


	async def get_block(self, block_index=""):
		return await self.req(
			{"method": "get_block", "params": {"block_index": block_index}}
		)


	async def get_confirmations(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_confirmations",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def get_mc_protocol_transaction(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_mc_protocol_transaction",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def get_mc_protocol_txo(self, txo_id=""):
		return await self.req(
			{"method": "get_mc_protocol_txo", "params": {"txo_id": txo_id}}
		)


	async def get_transaction_log(self, transaction_log_id=""):
		return await self.req(
			{
				"method": "get_transaction_log",
				"params": {"transaction_log_id": transaction_log_id},
			}
		)


	async def get_txo(self, txo_id=""):
		return await self.req({"method": "get_txo", "params": {"txo_id": txo_id}})


	async def get_txo_block_index(self, public_key=""):
		return await self.req(
			{"method": "get_txo_block_index", "params": {"public_key": public_key}}
		)


	async def get_txo_membership_proofs(self, outputs=""):
		return await self.req(
			{"method": "get_txo_membership_proofs", "params": {"outputs": outputs}}
		)


	async def import_account(
		self,
		mnemonic="",
		key_derivation_version="",
		name="",
		first_block_index="",
		next_subaddress_index="",
		fog_info="",
	):
		return await self.req(
			{
				"method": "import_account",
				"params": {
					"mnemonic": mnemonic,
					"key_derivation_version": key_derivation_version,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
					"fog_info": fog_info,
				},
			}
		)


	async def import_account_from_legacy_root_entropy(
		self,
		entropy="",
		name="",
		first_block_index="",
		next_subaddress_index="",
		fog_info="",
	):
		return await self.req(
			{
				"method": "import_account_from_legacy_root_entropy",
				"params": {
					"entropy": entropy,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
					"fog_info": fog_info,
				},
			}
		)


	async def import_view_only_account(
		self,
		view_private_key="",
		spend_public_key="",
		name="",
		first_block_index="",
		next_subaddress_index="",
	):
		return await self.req(
			{
				"method": "import_view_only_account",
				"params": {
					"view_private_key": view_private_key,
					"spend_public_key": spend_public_key,
					"name": name,
					"first_block_index": first_block_index,
					"next_subaddress_index": next_subaddress_index,
				},
			}
		)


	async def sample_mixins(self, num_mixins="", excluded_outputs=""):
		return await self.req(
			{
				"method": "sample_mixins",
				"params": {"num_mixins": num_mixins, "excluded_outputs": excluded_outputs},
			}
		)


	async def submit_transaction(
		self,
		tx_proposal={
			"input_txos": [],
			"payload_txos": [],
			"change_txos": [],
			"fee_amount": {"value": "", "token_id": ""},
			"tombstone_block_index": "",
			"tx_proto": "",
		},
		comment="",
		account_id="",
	):
		return await self.req(
			{
				"method": "submit_transaction",
				"params": {
					"tx_proposal": tx_proposal,
					"comment": comment,
					"account_id": account_id,
				},
			}
		)


	async def verify_address(self, address=""):
		return await self.req({"method": "verify_address", "params": {"address": address}})

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(FullServiceAPIv2().run())