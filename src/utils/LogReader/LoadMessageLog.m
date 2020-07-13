function Log = LoadMessageLog( Filename, DF, ignore_type_list)

% Log = LoadMessageLog( Filename, DF)
%
% Loads the binary Dragonfly message log in Filename and converts it to a matlab 
% data structure, organized by message type, so it is easy to look at
% data associated with any particular message type.
% Dragonfly is a structure containing Dragonfly message definitions (saved from a
% matlab module at runtime when Filename was recorded.

% Meel Velliste 12/29/2008

if ~exist('ignore_type_list', 'var')
    ignore_type_list = {};
end

RawLog = LoadRawMessageLog( Filename, DF, ignore_type_list);
Log = OrganizeLogByMsgType( RawLog, DF);
