@rem gyp.bat --depth=. -Icommon.gypi  -Dlibrary=shared_library -Dtarget_arch=x64 --build=debug leveldb.gyp

cd %~dp0/builds/windows/debug
arena_test.exe
autocompact_test.exe
bloom_test.exe
cache_test.exe
coding_test.exe
corruption_test.exe
crc32c_test.exe
c_test.exe
dbformat_test.exe
db_bench.exe
db_test.exe
env_test.exe
filename_test.exe
filter_block_test.exe
issue178_test.exe
issue200_test.exe
leveldbutil.exe
log_test.exe
skiplist_test.exe
table_test.exe
version_edit_test.exe
version_set_test.exe
write_batch_test.exe
cd %~dp0