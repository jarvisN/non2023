#include "RFID.h"

PN532_I2C pn532i2c(Wire);
PN532 nfc(pn532i2c);

bool RFIDLIB::init()
{
	nfc.begin();
	uint32_t versiondata = nfc.getFirmwareVersion();
	if (!versiondata)
	{
		return false;
	}

	nfc.setPassiveActivationRetries(0xFF);
	nfc.SAMConfig();

	return true;
}

void RFIDLIB::getIdHex(String &id, boolean &success, const uint32_t &timeout)
{
	_id = "";
	_success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &_uid[0], &_uidLength, timeout);
	if (_success)
	{
		for (uint8_t i = 0; i < _uidLength; i++)
		{
			if (_uid[i] < 16)
			{
				_id += "0" + String(_uid[i], HEX);
			}
			else
			{
				_id += String(_uid[i], HEX);
			}
		}
		_id.toUpperCase();
		id = _id;
		success = true;
	}
	else
	{
		success = false;
	}
}

void RFIDLIB::getIdDecimal(String &id, boolean &success, const uint32_t &timeout)
{
	_id = "";
	_success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &_uid[0], &_uidLength, timeout);
	if (_success)
	{
		for (uint8_t i = 0; i < _uidLength; i += 2)
		{
			_result = _uid[i] << 8 | _uid[i + 1];
			_id += String(_result);
		}
		id = _id;
		success = true;
	}
	else
	{
		success = false;
	}
}
