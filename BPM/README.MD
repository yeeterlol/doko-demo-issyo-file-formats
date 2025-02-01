# BP(M) (internal name: BIO Packman)
This is the main file format that all Doko Demo Issyo games package their assets in starting at Doko Demo Issyo: Toro to Ippai.

The internal process is that it gets compiled from a .KS (KsPlay Script File) into a BPM from KS files.

### Structs
Recovered from 2006 Mainichi Issho debug symbols[^1]
```c
struct PackedHeader {
    uint32_t file_count;
    uint32_t file_info_count;
    uint32_t file_name_buf_size;
    uint32_t offset_file_data_start;
};

struct PackedFileInfo {
    uint32_t offset_file_name;
    uint32_t offset_file_data;
    uint32_t file_data_size;
    uint32_t next_index;
};
```

## 1.0
The original file format used in all PSP and Vita games which also include BeXide-related games. 
### Encryption
In v1.0 of BPM, there is uint32 encryption of all offsets. Each byte needs to be bitshifted and get bitwised OR operation to get the real offset.

*example of decryption by bpar (Nekobit)*
```c
unsigned
dec_uint(unsigned char* arr, size_t len)
{
	unsigned res = 0;
	for (size_t i = 0; i < len; ++i)
	{
		res |= arr[i] << (i*8);
	}
	return res;
}
```



## 1.1
A Big-Endian ported version of BPM for the PS3, known for being very buggy.[^2]

Encryption has been removed from BPM 1.1. All offsets are unencrypted.
### Checksum zigzag index pattern
*WIP: Document more about how this pattern works and see if 1.0 included this checksum pattern, from Nekobit's comments, he seems that he forgot to calculate the checksum. The checksum calculation also needs to be more accurate. It works 95% of the time.*

The 0xC struct (next_index) is a checksum based on the name, size of file, and the file count.

If the 0xC bytes has FF FF FF FF then it is padding bytes in order to keep the pattern going, the game will automatically ignore them. **DO NOT UNDER ANY CIRCUMSTANCES REPLACE ALL FILE INFO CHECKSUMS WITH FF FF FF FF, YOUR GAME WILL CRASH.** 

Every 2 file infos, the game will automatically calculate a checksum and the resulting  and check. If the checksum fails then the BPM will refuse to load. 







[^1]: https://debugging.games
[^2]: On the 18th December 2006 broadcast (episode 40), a bug occurred that caused Kuro to remain in the room even after the broadcast had finished, which was fixed by the morning (translated from https://ja.wikipedia.org/wiki/トロ・ステーション)