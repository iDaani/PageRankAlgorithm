package uk.ac.qub.csc3021.graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;

// This class represents the adjacency matrix of a graph as a sparse matrix
// in compressed sparse columns format (CSC). The incoming edges for each
// vertex are listed.
public class SparseMatrixCSC extends SparseMatrix {
    // TODO: variable declarations
	int[] index_array;
	int[] source_array;
    // ...
    int num_vertices; // Number of vertices in the graph
    int num_edges;    // Number of edges in the graph

    public SparseMatrixCSC( String file ) {
	try {
	    InputStreamReader is
		= new InputStreamReader( new FileInputStream( file ), "UTF-8" );
	    BufferedReader rd = new BufferedReader( is );
	    readFile( rd );
	} catch( FileNotFoundException e ) {
	    System.err.println( "File not found: " + e );
	    return;
	} catch( UnsupportedEncodingException e ) {
	    System.err.println( "Unsupported encoding exception: " + e );
	    return;
	} catch( Exception e ) {
	    System.err.println( "Exception: " + e );
	    return;
	}
    }

    int getNext( BufferedReader rd ) throws Exception {
	String line = rd.readLine();
	if( line == null )
	    throw new Exception( "premature end of file" );
	return Integer.parseInt( line );
    }

    void readFile( BufferedReader rd ) throws Exception {
	String line = rd.readLine();
	if( line == null )
	    throw new Exception( "premature end of file" );
	if( !line.equalsIgnoreCase( "CSC" ) && !line.equalsIgnoreCase( "CSC-CSR" ) )
	    throw new Exception( "file format error -- header" );
	
	num_vertices = getNext(rd);
	num_edges = getNext(rd);

	// TODO: allocate data structures
	// ...
		index_array = new int[num_vertices + 1];
		source_array = new int[num_edges];
		int sourceCounter = 0;

	for( int i=0; i < num_vertices; ++i ) {
	    line = rd.readLine();
	    if( line == null )
		throw new Exception( "premature end of file" );
	    String elm[] = line.split( " " );
	    assert Integer.parseInt( elm[0] ) == i : "Error in CSC file";
		index_array[i] = sourceCounter;
	    for( int j=1; j < elm.length; ++j ) {
		int src = Integer.parseInt( elm[j] );
		// TODO:
		//    Record an edge from source src to destination i
		// ...
			source_array[sourceCounter] = src;
			sourceCounter++;
	    }
	}
		index_array[num_vertices] = num_edges;
    }

    // Return number of vertices in the graph
    public int getNumVertices() { return num_vertices; }

    // Return number of edges in the graph
    public int getNumEdges() { return num_edges; }


    // Auxiliary function for PageRank calculation
    public void calculateOutDegree( int outdeg[] ) {
	// TODO:
	//    Calculate the out-degree for every vertex, i.e., the
	//    number of edges where a vertex appears as a source vertex.
	// ...

		for (int i = 0; i < num_edges; i++) {
			outdeg[source_array[i]] = outdeg[source_array[i]] + 1;
		}
    }
    
    public void edgemap( Relax relax ) {
	// TODO:
	//    Iterate over all edges in the sparse matrix and call "relax"
	//    on each edge.
	// ...

		for (int i = 0; i < num_vertices; ++i) {
			int start_position = index_array[i];
			int end_position = index_array[i+1];

			for (int j = start_position; j < end_position; ++j) {
				relax.relax(source_array[j], i);
			}
		}
    }

    public void ranged_edgemap( Relax relax, int from, int to ) {
	// Only implement for parallel/concurrent processing
	// if you find it useful. Not relevant for the first assignment.
	// TODO:
	//    Iterate over partition indicated by from...to and calculate
	//    the contribution to the new PageRank value of a destination
	//    vertex made by the corresponding source vertex
    }
}

