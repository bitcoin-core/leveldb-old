{
  'variables':{
  },
  'targets': [
    
    ########################################
    # level-db static library
    ########################################
    {
      'target_name': 'libleveldb',
      'product_name': 'libleveldb',
      'type': 'static_library',

      'dependencies': [
      ],
     'export_dependent_settings': [
      ],

      'conditions': [
        ['OS=="linux"', {
          'defines': [
            'PLATFORM_LINUX',
          ],
          'cflags': [
            '-std=gnu99',
          ],
        }],
        ['OS=="win"', {
          'defines': [
            'LEVELDB_PLATFORM_WINDOWS',
          ],
          'sources': [
			'port/port_win.h',
			'port/port_win.cc',
          ],
          'include_dirs': [
			'port/win',
          ],
		  'direct_dependent_settings': {
			'include_dirs': [ ],
            'libraries': [ 'shlwapi.lib' ],
            'defines': [ 'LEVELDB_PLATFORM_WINDOWS', ],
		  },
          'libraries': [ 'shlwapi.lib' ]
        }, { # OS != "win",
          'defines': [
            'PLATFORM_POSIX',
          ],
        }],
      ],

      'include_dirs': [
		'include',
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],

      'direct_dependent_settings': {
        'include_dirs': [
          'include',
          '<(SHARED_INTERMEDIATE_DIR)',
        ],
      },
      
      'sources': [
		'include/leveldb/c.h', 
		'include/leveldb/cache.h', 
		'include/leveldb/comparator.h', 
		'include/leveldb/db.h', 
		'include/leveldb/env.h', 
		'include/leveldb/filter_policy.h', 
		'include/leveldb/iterator.h', 
		'include/leveldb/options.h', 
		'include/leveldb/slice.h', 
		'include/leveldb/status.h', 
		'include/leveldb/table.h', 
		'include/leveldb/table_builder.h', 
		'include/leveldb/write_batch.h', 
		'port/port.h', 
		'db/builder.h', 
		'db/dbformat.h', 
		'db/db_impl.h', 
		'db/db_iter.h', 
		'db/filename.h', 
		'db/log_format.h', 
		'db/log_reader.h', 
		'db/log_writer.h', 
		'db/memtable.h', 
		'db/skiplist.h', 
		'db/snapshot.h', 
		'db/table_cache.h', 
		'db/version_edit.h', 
		'db/version_set.h', 
		'db/write_batch_internal.h', 
		'db/builder.cc', 
		'db/c.cc', 
		'db/db_impl.cc', 
		'db/db_iter.cc', 
		'db/dbformat.cc', 
		'db/filename.cc', 
		'db/log_reader.cc', 
		'db/log_writer.cc', 
		'db/memtable.cc', 
		'db/repair.cc', 
		'db/table_cache.cc', 
		'db/version_edit.cc', 
		'db/version_set.cc', 
		'db/write_batch.cc', 
		'table/block.h', 
		'table/block_builder.h', 
		'table/filter_block.h', 
		'table/format.h', 
		'table/iterator_wrapper.h', 
		'table/merger.h', 
		'table/two_level_iterator.h', 
		'table/block.cc', 
		'table/block_builder.cc', 
		'table/filter_block.cc', 
		'table/format.cc', 
		'table/iterator.cc', 
		'table/merger.cc', 
		'table/table.cc', 
		'table/table_builder.cc', 
		'table/two_level_iterator.cc', 
		'util/arena.h', 
		'util/coding.h', 
		'util/crc32c.h', 
		'util/hash.h', 
		'util/histogram.h', 
		'util/logging.h', 
		'util/mutexlock.h', 
		'util/posix_logger.h', 
		'util/random.h', 
		'util/arena.cc', 
		'util/bloom.cc', 
		'util/cache.cc', 
		'util/coding.cc', 
		'util/comparator.cc', 
		'util/crc32c.cc', 
		'util/env.cc', 
		'util/env_posix.cc', 
		'util/env_win.cc', 
		'util/filter_policy.cc', 
		'util/hash.cc', 
		'util/histogram.cc', 
		'util/logging.cc', 
		'util/options.cc', 
		'util/status.cc', 
      ],

    }, # libleveldb static library

    ########################################
    # db_bench
    ########################################
    {
      'target_name': 'db_bench',
      'product_name': 'db_bench',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/db_bench.cc',
      ],
    }, # db_bench

    ########################################
    # db_bench_sqlite3
    ########################################
    {
      'target_name': 'db_bench_sqlite3',
      'product_name': 'db_bench_sqlite3',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'doc/bench/db_bench_sqlite3.cc',
      ],
    }, # db_bench_sqlite3

    ########################################
    # db_bench_tree_db
    ########################################
    {
      'target_name': 'db_bench_tree_db',
      'product_name': 'db_bench_tree_db',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'doc/bench/db_bench_tree_db.cc',
      ],
    }, # db_bench_tree_db

    ########################################
    # leveldbutil
    ########################################
    {
      'target_name': 'leveldbutil',
      'product_name': 'leveldbutil',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/leveldb_main.cc',
      ],
    }, # leveldbutil
    
    ########################################
    # arena_test
    ########################################
    {
      'target_name': 'arena_test',
      'product_name': 'arena_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/arena_test.cc',
      ],
    }, # arena_test

    ########################################
    # autocompact_test
    ########################################
    {
      'target_name': 'autocompact_test',
      'product_name': 'autocompact_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],

      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/autocompact_test.cc',
      ],
    }, # autocompact_test
    
    ########################################
    # bloom_test
    ########################################
    {
      'target_name': 'bloom_test',
      'product_name': 'bloom_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/bloom_test.cc',
      ],
    }, # bloom_test

    ########################################
    # c_test
    ########################################
    {
      'target_name': 'c_test',
      'product_name': 'c_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/c_test.c',
      ],
    }, # c_test
    
    ########################################
    # cache_test
    ########################################
    {
      'target_name': 'cache_test',
      'product_name': 'cache_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/cache_test.cc',
      ],
    }, # cache_test
    
    ########################################
    # coding_test
    ########################################
    {
      'target_name': 'coding_test',
      'product_name': 'coding_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/coding_test.cc',
      ],
    }, # coding_test
    
    ########################################
    # corruption_test
    ########################################
    {
      'target_name': 'corruption_test',
      'product_name': 'corruption_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/corruption_test.cc',
      ],
    }, # corruption_test
    
    ########################################
    # crc32c_test
    ########################################
    {
      'target_name': 'crc32c_test',
      'product_name': 'crc32c_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/crc32c_test.cc',
      ],
    }, # crc32c_test
    
    ########################################
    # db_test
    ########################################
    {
      'target_name': 'db_test',
      'product_name': 'db_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/db_test.cc',
      ],
    }, # db_test
    
    ########################################
    # dbformat_test
    ########################################
    {
      'target_name': 'dbformat_test',
      'product_name': 'dbformat_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/dbformat_test.cc',
      ],
    }, # dbformat_test
    
    ########################################
    # env_test
    ########################################
    {
      'target_name': 'env_test',
      'product_name': 'env_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'util/env_test.cc',
      ],
    }, # env_test
    
    ########################################
    # filename_test
    ########################################
    {
      'target_name': 'filename_test',
      'product_name': 'filename_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/filename_test.cc',
      ],
    }, # filename_test
    
    ########################################
    # filter_block_test
    ########################################
    {
      'target_name': 'filter_block_test',
      'product_name': 'filter_block_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'table/filter_block_test.cc',
      ],
    }, # filter_block_test
    
    ########################################
    # issue178_test
    ########################################
    {
      'target_name': 'issue178_test',
      'product_name': 'issue178_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'issues/issue178_test.cc',
      ],
    }, # issue178_test
    
    ########################################
    # issue200_test
    ########################################
    {
      'target_name': 'issue200_test',
      'product_name': 'issue200_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'issues/issue200_test.cc',
      ],
    }, # issue200_test
    
    ########################################
    # log_test
    ########################################
    {
      'target_name': 'log_test',
      'product_name': 'log_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/log_test.cc',
      ],
    }, # log_test
    
    ########################################
    # table_test
    ########################################
    {
      'target_name': 'table_test',
      'product_name': 'table_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'table/table_test.cc',
      ],
    }, # table_test
    
    ########################################
    # skiplist_test
    ########################################
    {
      'target_name': 'skiplist_test',
      'product_name': 'skiplist_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/skiplist_test.cc',
      ],
    }, # skiplist_test
    
    ########################################
    # version_edit_test
    ########################################
    {
      'target_name': 'version_edit_test',
      'product_name': 'version_edit_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/version_edit_test.cc',
      ],
    }, # version_edit_test
    
    ########################################
    # version_set_test
    ########################################
    {
      'target_name': 'version_set_test',
      'product_name': 'version_set_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/version_set_test.cc',
      ],
    }, # version_set_test
    
    ########################################
    # write_batch_test
    ########################################
    {
      'target_name': 'write_batch_test',
      'product_name': 'write_batch_test',
      'type': 'executable',

      'dependencies': [
        'libleveldb',
      ],
      
      'include_dirs': [
		'.',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      
      'sources': [
        'util/testharness.h',
        'util/testutil.h',
        'util/testharness.cc',
        'util/testutil.cc',
        'db/write_batch_test.cc',
      ],
    }, # write_batch_test
  ],
}