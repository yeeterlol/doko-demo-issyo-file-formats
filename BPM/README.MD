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

## Hashing
A very important thing to know that all of the PackMan file entrys are a hash table for optimization.  

At 0xC for every PackedFileInfo, there is a next_index uint32. This is the next index to a Linked List.

If it is just `FF FF FF FF` then it is an empty entry, anything else should be considered an entry if it is below or equal to the amount of items in the file.

The hash is calculated by the BKDR hash which comes from The C Programming Language book which it is modulo operated by the amount of items. 

The game searches for items by calculating a hash, going to the index and calculating `File name offset + Offset file name`, if it does not match, it goes to the index of 0xC while checking if it is en empty entry, this repeats forever until an empty entry is found or the file is matched.

There is a provided **Python script** to automatically calculate hashes for you.



[^1]: https://debugging.games
